from src.models.text_transformation import NewTextTransformation


async def test_get_text_transformations__returns_emty_list__if_dont_exist(text_transformations_repo):
    guest_text_transfromations = await text_transformations_repo.get_guest_text_transformations()

    assert not guest_text_transfromations


async def test_get_text_transformations__returns_1_transformation__if_exists(
    make_text_db_record,
    text_transformations_repo,
):
    await make_text_db_record(
        original_text='Прекрасный текст',
        transformed_text='Безумный текст',
        user_id=None,
    )
    guest_text_transfromations = await text_transformations_repo.get_guest_text_transformations()

    assert len(guest_text_transfromations) == 1


async def test_get_text_transformations__returns_text_transformation_with_expected_original_text__if_exists(
    make_text_db_record,
    text_transformations_repo,
):
    await make_text_db_record(
        original_text='Прекрасный текст',
        transformed_text='Безумный текст',
        user_id=None,
    )
    guest_text_transfromations = await text_transformations_repo.get_guest_text_transformations()

    assert guest_text_transfromations[0].original_text == 'Прекрасный текст'


async def test_get_text_transformations__returns_text_transformation_with_expected_transformed_text__if_exists(
    make_text_db_record,
    text_transformations_repo,
):
    await make_text_db_record(
        original_text='Прекрасный текст',
        transformed_text='Безумный текст',
        user_id=None,
    )
    guest_text_transfromations = await text_transformations_repo.get_guest_text_transformations()

    assert guest_text_transfromations[0].transformed_text == 'Безумный текст'


async def test_add_text_transformation__results_in__new_corresponding_table_record(text_transformations_repo, db):
    new_text_transformation = NewTextTransformation(
        original_text='Прекрасный текст',
        transformed_text='Безумный текст',
        user_id=None,
    )
    await text_transformations_repo.add_text_transformation(new_text_transformation=new_text_transformation)

    query = 'SELECT * FROM texts'
    async with db.connection() as connection:
        rows = await connection.fetch_all(query=query)

    assert len(rows) == 1
