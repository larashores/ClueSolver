#pragma once

#include <vector>

#include "person.h"
#include "weapon.h"
#include "room.h"


class Deck
{
public:
    Deck();

    std::vector<const Card*> get_all_cards() const;
    int size() const;

    const std::vector<Person> people;
    const std::vector<Weapon> weapons;
    const std::vector<Room> rooms;
};
