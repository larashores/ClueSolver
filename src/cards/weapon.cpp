#include "../../include/cards/weapon.h"

Weapon::Weapon(const std::string& name) :
    Card{name, Card::WEAPON}
{

}

Weapon operator"" _w(const char* name, std::size_t)
{
    return Weapon{name};
}
