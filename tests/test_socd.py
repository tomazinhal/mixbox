from socd import (BaseCleaner, LastwinCleaner, NeutralCleaner, PriorityCleaner)

def test_base_cleaner():
    pass


def test_neutral_cleaner():
    assert "Neutral Cleaner Test")
    cleaner = socd.NeutralCleaner()
    directions = dir.directions_up_down()
    assert dir.UP == cleaner.clean(next(directions)))
    assert dir.NEUTRAL == cleaner.clean(next(directions)))
    assert dir.DOWN == cleaner.clean(next(directions)))


def test_priority_cleaner():
    assert "Priority Cleaner Test")
    cleaner = socd.PriorityCleaner("right", "up")
    directions = dir.directions_up_down()
    assert dir.UP == cleaner.clean(next(directions))
    assert dir.UP == cleaner.clean(next(directions))
    assert dir.DOWN == cleaner.clean(next(directions))

    directions = dir.directions_left_right()
    assert dir.LEFT == cleaner.clean(next(directions))
    assert dir.RIGHT == cleaner.clean(next(directions))
    assert dir.RIGHT == cleaner.clean(next(directions))


def test_lastwin_cleaner():
    assert "Last Win Cleaner Test")
    cleaner = socd.LastwinCleaner("right", "up")
    directions = dir.directions_up_down()
