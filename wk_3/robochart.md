# RobotChart Basics

## Robotic Platform

Records assumptions about capabilities of hardware/embedded system.

* Events provided/accepted
* Supported operations
* Variables/constants

A module defined when composed with 1+ controllers.
Single point of interaction with env.

## Interfaces

Groups constants variables, operations and events.

Interface Types:

* Provided - groups constants, variables an operations
* Required - groups constants, variables and operations
* Defined - groups constants, variables and events

## Types

Constructors:

* Primitive - nothing else about the type
* Records - named components
* Enumeration - group of constants

Toolkits:

* API for collections, functions, relations, etc.
* Sequences
* Sets
* Based on Z notation

## Module

Main structuring element for single robotic system, characterised by interactions
between:

1. Robotic platform, recording services used by software in terms of shared
variables, events and operations
2. 1+ controllers, specifying behaviour of interest as a composition of 1+ state
state machines

## Controller

Models specific behaviour.
Contains constants, variables, operations and events declared explicitly or by 
interface.
Multiple state machines used to define behaviour.
Synchronous or asynchronous communication between controllers. Communication between
state machines is synchronous

## State Machines

Main behavioural specification construct.

* Self-contained
* Describes a data model and associated behaviour

Behaviour: sequence of shared variable updates, operation calls and events

* Next step of behaviour defined according to current state
* State captures consequences of behaviour so far
* Parallelism to identify several behaviour threads
* Clocks to define timed behaviours

## States and Junctions

### Junctions

Represent a decision point (e.g. if/else)

* Initial junction indicates start of control flow
* Transitions out of junction must form a cover

### States

Have names and actions, e.g. entry, during and exit.

## Transitions

Directed relationship between nodes (states and junctions).

Transitions have a label: `trigger #Clock [guard] / action`

* Trigger - event, possibly defining inputs
* Clock - reset when transition is triggered
* Guard - bool condition
* Action - statement including assignment, if-statement, output comms, operation
* call, etc.

All parts to a label are optional.

## Action Language

* Do nothing - `skip`
* Assignment - `x = 1`
* Sequential composition - `x = 1 ; skip`
* If statement - `if x > 1 then x = x - 1 else x = x + 1`
* Input comms - `ev?x`
* Output comms - `ev!1`
* Operation call - `op(1)`
* Delay - `wait(1)`
* Clock reset - `#C`

## Expression Language

* Sequence - `<1, 2, 3>`
* Set - `{0, 1}`
* Tuple - `(| 0, 1 |)`
* Concatenation - `<1> ^ <2>`
* Record - `Twist(| linear = _, angular = _ |)`
* Enumeration - `Location::Left`
* Clock value - `since(Clock) or sinceEntry(State)`
* Array access - `e[i]`
* Vector - `[| v1, _, vn |]`
* Matric - `[| v11, _, v1n; _; vm1, _, vmn |]`

