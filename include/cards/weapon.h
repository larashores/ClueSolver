#pragma once

#include "card.h"

class Weapon : public Card
{
public:
    explicit Weapon(const std::string& name);
};

Weapon operator"" _w(const char*, std::size_t);