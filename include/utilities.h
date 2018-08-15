#include <string>
#include <vector>
#include <iostream>

namespace util {
    template<typename T>
    T* address_of(T& val)
    {
        return &val;
    }

    template<typename Iterable, typename ConversionFunc>
    std::string list_string(Iterable items, ConversionFunc func)
    {
        std::string string;
        for(auto i = 0u; i < items.size(); i++)
        {
            auto it {items.begin()};
            std::advance(it, i);
            string += std::to_string(i + 1);
            string += ". ";
            string += func(*it);
            if (i != items.size() - 1)
            {
                string += "\n";
            }
        }
        return string;
    }
    template<typename Iterable>
    std::string list_string(Iterable items)
    {
        return list_string(items, [&](auto val){return std::string(val);});
    }

    template<typename FuncType>
    int ask_for_int(const std::string& initial_msg, FuncType condition)
    {
        std::cout << initial_msg << std::endl;
        while (true)
        {
            std::string input;
            std::getline(std::cin, input);
            try
            {
                int value {std::stoi(input)};
                if (condition(value))
                {
                    return value;
                } else
                {
                    std::cout << "Invalid Answer. Try Again." << std::endl;
                }
            } catch (std::invalid_argument& e)
            {
                std::cout << "Error Processing, Try Again." << std::endl;
            }
        }
    }

    inline int ask_for_int(const std::string& initial_msg, int min, int max)
    {
        return ask_for_int(initial_msg, [=](int value){return value >= min && value <= max;});
    }

    inline std::string ask_for_string(const std::string& msg)
    {
        std::cout << msg << std::endl;
        std::string string;
        std::getline(std::cin, string);
        return string;
    }
}