#pragma once

#include <string>


class Card
{
public:
    enum CardType {PERSON=0, WEAPON, ROOM};
    const std::string name;
    const CardType type;

    explicit operator std::string() const;

protected:
    Card(const std::string& name_, CardType type_);
};
