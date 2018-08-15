#include "../../include/cards/person.h"


Person::Person(const std::string& name) :
    Card{name, Card::PERSON}
{

}

Person operator"" _p(const char* name, std::size_t)
{
    return Person{name};
}
