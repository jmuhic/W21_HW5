"""
############################## Homework #1 ##############################

% Student Name: Jana Muhic

% Student Unique Name: jmuhic

% Lab Section 00X: 006

% I worked with the following classmates: N/A

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")

    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"

        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q1 = hw5_cards.Card(0, 12)

        self.assertEqual(q1.rank_name, "Queen")

        return q1.rank_name, "Queen"

    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"

        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        # Card(suit, rank)
        q2 = hw5_cards.Card(1, 12)

        self.assertEqual(q2.suit_name, "Clubs")

        return q2.suit_name, "Clubs"


    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"


        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        # Card(suit, rank)
        temp = hw5_cards.Card(3, 13)
        q3 = temp.__str__()  # formatted print

        self.assertEqual(q3, "King of Spades")

        return q3, "King of Spades"

    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a deck instance, it will have 52 cards in its cards instance variable

        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        # creation and len count of deck instance
        deck = hw5_cards.Deck()
        deck_count = len(deck.cards)

        self.assertEqual(deck_count, 52)

        return deck_count, 52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.

        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q5 = hw5_cards.Deck()
        dealt_card = q5.deal_card()

        # testing 'dealt_card' is a Card instance
        self.assertIsInstance(dealt_card, hw5_cards.Card)

        return dealt_card, hw5_cards.Card


    def test_q6(self):
        '''
        1. fill in your test method for question 6:

        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.

        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q6 = hw5_cards.Deck()
        q6_init_count = len(q6.cards)
        q6.deal_card()
        q6_end_count = len(q6.cards)

        # Testing that end count is one fewer than the inital
        self.assertEqual((q6_init_count - 1), q6_end_count)

        return (q6_init_count - 1), q6_end_count


    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)


        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q7 = hw5_cards.Deck()
        dealt_card = q7.deal_card()
        deckInitialCount = len(q7.cards)

        # Replace with same card dealt
        q7.replace_card(dealt_card)
        deckEndCount = len(q7.cards)

        # Testing that that end count is one greater than the initial
        # Expected count value is '52'
        self.assertEqual((deckInitialCount + 1), deckEndCount, 52)

        return (deckInitialCount +  1), deckEndCount, 52


    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)


        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q8 = hw5_cards.Deck()
        randomCard = hw5_cards.Card(0 , 13)
        initDeckCount = len(q8.cards)

        # Attempt to replace with card already in full Deck
        q8.replace_card(randomCard)

        finalDeckCount = len(q8.cards)

        # Test that 'replace_card' method did not change deck size
        # the card is already in the deck (full Deck)
        self.assertEqual(initDeckCount, finalDeckCount)

        return initDeckCount, finalDeckCount


    def test_q8_alt(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)


        2. remove the pass command

        3. uncomment the return command and
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q8 = hw5_cards.Deck()
        q8.deal_card()
        newDeck = q8.cards
        newDeckCount = len(newDeck)

        # Attempt to replace with card already in newDeck
        for c in newDeck:
            q8.replace_card(c)

        finalDeckCount = len(q8.cards)

        # Test that 'replace_card' method did not change deck size
        # if the card is already in the deck
        self.assertEqual(newDeckCount, finalDeckCount)

        return newDeckCount, finalDeckCount


if __name__=="__main__":
    unittest.main()