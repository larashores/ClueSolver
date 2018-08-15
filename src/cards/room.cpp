#include "../../include/cards/room.h"

Room::Room(const std::string& name) :
    Card{name, Card::ROOM}
{

}

Room operator"" _r(const char* name, std::size_t)
{
    return Room{name};
}
