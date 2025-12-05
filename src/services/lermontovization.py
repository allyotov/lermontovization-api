import logging
from functools import lru_cache
from typing import Literal

import pymorphy2
from natasha import Doc, NewsEmbedding, NewsMorphTagger, Segmenter

from src.services.tags import pos_of_interest, redundant_grammemes, shaping_grammemes

logger = logging.getLogger(__name__)
TEMP_RESULT_TEXT_TEMPLATE = """Говорит lermontovization-api: лермонтовизация текста сейчас находится в разработке.
Скоро мы будем присылать вам лермонтовизированный вариант вашего текста. Пока вернём его как есть: {input_text}"""

TEMP_DEMO_RESULT_TEXT_TEMPLATE = """Говорит lermontovization-api: демонстрационная лермонтовизация текста
сейчас находится в разработке. Скоро мы будем присылать вам лермонтовизированный вариант вашего текста.
Пока вернём его как есть: {input_text}"""


class LermontovizationService:
    def __init__(self):
        self._morph = pymorphy2.MorphAnalyzer(lang='ru')
        insane = self._morph.parse('безумный')[0]
        unworldy = self._morph.parse('неземной')[0]
        self._unworldy_additional_epithet = self._morph.parse('неотмирен')[0]
        self._epithets = (insane, unworldy)
        self._poetic_forms = {'кратк': 'краток'}

        self._segmenter = Segmenter()
        self._emb = NewsEmbedding()
        self._morph_tagger = NewsMorphTagger(self._emb)

    def process_text(self, text: str) -> str:
        # TODO: исходный текст и его лермонтовизированный вариант должны сохраняться в базу данных.
        return self._process_text(text_str=text)

    def process_text_demo(self, text: str) -> str:
        return self._process_text(text_str=text)

    def _process_text(self, text_str: str) -> str:
        """Лермонтовизировать заданный текст.

        То есть вернуть текст, в котором все прилагательные заменены на "безумный" и "неземной" в той же форме, которую
        имело исходное прилагательное.
        В качестве краткой формы эпитета "неземной" будет использоваться слово "неотмирен".
        """
        is_epithet_second = False

        doc = Doc(text_str)
        doc.segment(self._segmenter)
        doc.tag_morph(self._morph_tagger)

        resulting_words = []
        for token in doc.tokens:
            word = token.text
            current_word = word

            if token.pos == 'ADJ':
                current_word = self._process_adjective(
                    adjective=current_word,
                    tag=token.pos,
                    is_epithet_second=is_epithet_second,
                )
                is_epithet_second = not is_epithet_second

            elif token.pos == 'PUNCT' and resulting_words:
                resulting_words[-1] = '{word}{punct_sign}'.format(word=resulting_words[-1], punct_sign=current_word)
                continue
            resulting_words.append(current_word)
        """
        Пока будем предполагать, что между словами всегда не более одного пробела, а знаки препинания ставятся сразу
        после слов без пробелов.
        TODO: 1) добавить сохранение количества пробелов исходного текста;
        TODO: 2) добавить сохранение дополнительных символов исходного текста; 
        """
        return ' '.join(resulting_words)

    def _process_adjective(self, adjective: str, tag: str, is_epithet_second: bool) -> str:
        _raise_value_error_if_word_not_adjective(word=adjective, tag=tag)

        adjective_initial_register_info = _get_word_register_info(word=adjective)
        epithet = self._replace_adjective_with_epithet(adjective, is_epithet_second=is_epithet_second)

        epithet = _apply_word_register_info(word=epithet, word_register_info=adjective_initial_register_info)

        return epithet

    def _replace_adjective_with_epithet(self, adjective: str, is_epithet_second: bool = False) -> str:
        if adjective in self._poetic_forms:
            adjective = self._poetic_forms[adjective]

        adjective_parse = self._morph.parse(adjective)

        for parse in adjective_parse:
            if parse.tag.POS in pos_of_interest:
                tag_str = str(parse.tag)
                p_tag_pos = parse.tag.POS
                break

        else:
            raise ValueError(
                '"%s": часть речи преобразуемого слова должна быть "прилагательное" или "краткое прилагательное"',
                adjective,
            )

        grammemes = _get_grammems_from_tag_string(tag_str=tag_str)
        target_form_grammemes = _get_target_form_grammemes(grammemes=grammemes)

        epithet = self._get_epithet(is_epithet_second=is_epithet_second, p_tag_pos=p_tag_pos)
        return epithet.inflect(target_form_grammemes).word

    def _get_epithet(self, p_tag_pos: str, is_epithet_second: bool = False) -> str:
        epithet = self._epithets[is_epithet_second]
        if p_tag_pos == 'ADJS' and is_epithet_second:
            epithet = self._unearthly
        return epithet


def _get_grammems_from_tag_string(tag_str: str) -> list[str]:
    raw_grammem_strings = tag_str.split(',')
    grammems = []
    for grammem_string in raw_grammem_strings:
        new_grammems = [grammem_string]
        if ' ' in grammem_string:
            new_grammems = grammem_string.split(' ')

        grammems += new_grammems
    return grammems


def _get_target_form_grammemes(grammemes: list[str]) -> set[str]:
    target_form_grammemes = []
    word_redundant_grammemes = []
    unexplored_grammemes = []
    for grammem in grammemes:
        if grammem in shaping_grammemes:
            target_form_grammemes.append(grammem)
        elif grammem in redundant_grammemes:
            word_redundant_grammemes.append(grammem)
        else:
            unexplored_grammemes.append(grammem)

    return set(target_form_grammemes)


def _raise_value_error_if_word_not_adjective(word: str, tag: str) -> None:
    if tag != 'ADJ' and tag != 'ADJS':
        raise ValueError('Слово "{word}" не является прилагательным!'.format(word=word))


def _get_word_register_info(word: str) -> Literal['lowercase', 'uppercase', 'capitalized']:
    word_register_info = 'lowercase'
    if word.isupper():
        word_register_info = 'uppercase'
    elif word[0].isupper():
        word_register_info = 'capitalized'
    return word_register_info


def _apply_word_register_info(word: str, word_register_info: Literal['lowercase', 'uppercase', 'capitalized']) -> str:
    if word_register_info == 'uppercase':
        word = word.upper()
    elif word_register_info == 'capitalized':
        word = word.capitalize()
    return word


@lru_cache()
def get_lermontovization_service():
    return LermontovizationService()
