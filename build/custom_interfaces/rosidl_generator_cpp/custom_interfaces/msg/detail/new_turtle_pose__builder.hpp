// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/NewTurtlePose.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/new_turtle_pose__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_NewTurtlePose_theta
{
public:
  explicit Init_NewTurtlePose_theta(::custom_interfaces::msg::NewTurtlePose & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::NewTurtlePose theta(::custom_interfaces::msg::NewTurtlePose::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::NewTurtlePose msg_;
};

class Init_NewTurtlePose_y
{
public:
  explicit Init_NewTurtlePose_y(::custom_interfaces::msg::NewTurtlePose & msg)
  : msg_(msg)
  {}
  Init_NewTurtlePose_theta y(::custom_interfaces::msg::NewTurtlePose::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_NewTurtlePose_theta(msg_);
  }

private:
  ::custom_interfaces::msg::NewTurtlePose msg_;
};

class Init_NewTurtlePose_x
{
public:
  explicit Init_NewTurtlePose_x(::custom_interfaces::msg::NewTurtlePose & msg)
  : msg_(msg)
  {}
  Init_NewTurtlePose_y x(::custom_interfaces::msg::NewTurtlePose::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_NewTurtlePose_y(msg_);
  }

private:
  ::custom_interfaces::msg::NewTurtlePose msg_;
};

class Init_NewTurtlePose_name
{
public:
  Init_NewTurtlePose_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NewTurtlePose_x name(::custom_interfaces::msg::NewTurtlePose::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_NewTurtlePose_x(msg_);
  }

private:
  ::custom_interfaces::msg::NewTurtlePose msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::NewTurtlePose>()
{
  return custom_interfaces::msg::builder::Init_NewTurtlePose_name();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__BUILDER_HPP_
