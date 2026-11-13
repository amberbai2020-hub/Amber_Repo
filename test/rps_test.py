
# this is the "test/rps_test.py" file...

from app.rps import determine_winner

#The test name has to start with test_
#The test must exist in the test directory
#Any function within the file must be called test_
#You may have multiple test functions
#Assert function expects the statement to be True

def test_winners():
    # tests for all edge cases:

    assert determine_winner(u="rock", c="rock") == "TIE GAME"
    assert determine_winner(u="rock", c="paper") == "COMPUTER WINS"
    assert determine_winner(u="rock", c="scissors") == "USER WINS"

    assert determine_winner(u="paper", c="rock") == "USER WINS"
    assert determine_winner(u="paper", c="paper") == "TIE GAME"
    assert determine_winner(u="paper", c="scissors") == "COMPUTER WINS"

    assert determine_winner(u="scissors", c="scissors") == "TIE GAME"
    assert determine_winner(u="scissors", c="paper") == "USER WINS"
    assert determine_winner(u="scissors", c="rock") == "COMPUTER WINS"