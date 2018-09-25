from flaskapp.models import Thing


def test_saving_and_retrieving_a_thing(db_session):
    thing = Thing(name='thing one')
    db_session.add(thing)
    db_session.commit()

    all_the_things = db_session.query(Thing).all()

    assert len(all_the_things) == 1


def test_saving_and_retrieving_another_thing(db_session):
    thing = Thing(name='thing two')
    db_session.add(thing)
    db_session.commit()

    all_the_things = db_session.query(Thing).all()

    assert len(all_the_things) == 1
