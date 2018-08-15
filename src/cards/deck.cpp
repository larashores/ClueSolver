#include "../../include/cards/deck.h"


Deck::Deck() :
    people{"Col. Mustard"_p ,
           "Prof, Plum"_p ,
           "Mr. Green"_p ,
           "Mrs. Peacock"_p ,
           "Mrs. Scarlet"_p ,
           "Mrs. White"_p},
    weapons{"Knife"_w,
            "Candlestick"_w,
            "Revolver"_w,
            "Rope"_w,
            "Lead Pipe"_w,
            "Wrench"_w},
    rooms{"Hall"_r,
          "Lounge"_r,
          "Dining Room"_r,
          "Kitchen"_r,
          "Ballroom"_r,
          "Conservatory"_r,
          "Billard Room"_r,
          "Library"_r,
          "Study"_r}
{

}

int Deck::size() const
{
    return static_cast<int>(people.size() + weapons.size() + rooms.size());
}

std::vector<const Card*> Deck::get_all_cards() const
{
    std::vector<const Card*> cards;
    for (auto& card: people)
    {
        cards.push_back(&card);
    }
    for (auto& card: weapons)
    {
        cards.push_back(&card);
    }
    for (auto& card: rooms)
    {
        cards.push_back(&card);
    }
    return cards;
}
