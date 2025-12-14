async def test_get_text_transformations(make_text_db_record, text_transformations_repo):
    # TODO: заполнить параметры, используя Faker
    await make_text_db_record(
        original_text='Прекрасный текст',
        transformed_text='Безумный текст',
        user_id=None,
    )
    guest_text_transfromation = await text_transformations_repo.get_guest_text_transformations()

    assert len(guest_text_transfromation) == 1
