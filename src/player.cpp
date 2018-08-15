#include "../include/player.h"


Player::Player(const std::string& name_, int num_cards_) :
    name{name_},
    num_cards{num_cards_}
{
}

Player::operator std::string() const
{
    return name;
}
