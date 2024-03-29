def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    if player_high_aces >0:
        if player_total <= 17:
            return True
        elif player_total <=21:
            return False
    else:
        # Check if hitting would keep the total below or equal to 16
        if player_total <= 16:
            return True
        # If the total is over 16, the player should not hit
        else:
            return False
