#include "../../include/cards/card.h"


Card::Card(const std::string& name_, CardType type_) :
        name{name_},
        type{type_}
{
}

Card::operator std::string() const
{
    return name;
}
