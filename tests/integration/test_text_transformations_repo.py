async def test_get_text_transformations(make_text_db_record, text_transformations_repo):
    make_text_db_record()  # TODO: заполнить параметры, используя Faker
    guest_text_transfromation = await text_transformations_repo.get_guest_text_transformations()

    assert len(guest_text_transfromation) == 1
