#pragma once

#include "card.h"


class Room : public Card
{
public:
    explicit Room(const std::string& name);
};

Room operator"" _r(const char*, std::size_t);
