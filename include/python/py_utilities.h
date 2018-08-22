#pragma once

#include <boost/python.hpp>
#include "cards/person.h"

namespace python {

template<typename Sequence>
boost::python::list stl2py(const Sequence& sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(arg);
    }
    return list;
}

template<typename Sequence>
boost::python::list stl2pyptr(Sequence sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(&arg);
    }
    return list;
}

template <typename T, typename std::enable_if_t<!std::is_pointer<T>::value>* = nullptr>
std::shared_ptr<T> to_shared_ptr(T& val)
{
    return std::shared_ptr<T>(&val, [=](auto){});
}

template <typename T, typename std::enable_if_t<std::is_pointer<T>::value>* = nullptr>
std::shared_ptr<T> to_shared_ptr(T& val)
{
    return std::shared_ptr<T>(val, [=](auto){});
}

template<typename Sequence>
boost::python::list to_ptr_list(Sequence& sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(to_shared_ptr(arg));
    }
    return list;
}

template<typename T>
long hash_object(const T& obj)
{
    return reinterpret_cast<std::uintptr_t>(&obj) / 8;
}

template<typename T>
bool equals_object(const T& obj1, const T& obj2)
{
    return &obj1 == &obj2;
}

}  // namespace