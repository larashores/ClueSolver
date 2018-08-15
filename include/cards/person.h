#pragma once

#include "card.h"


class Person : public Card
{
public:
    explicit Person(const std::string& name);
};

Person operator"" _p(const char*, std::size_t);
