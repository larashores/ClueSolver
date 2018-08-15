#pragma once

#include <set>

#include "cards/card.h"


struct Stats
{
    Stats& operator+=(const Stats& other);

    std::set<const Card*> positives;
    std::set<const Card*> negatives;
};

inline Stats& Stats::operator+=(const Stats& other)
{
    for (auto card: other.positives)
    {
        positives.insert(card);
    }
    for (auto card: other.negatives)
    {
        negatives.insert(card);
    }
    return *this;
}
