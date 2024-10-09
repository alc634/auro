#ifndef ROBOCALC_CONTROLLERS_CONTROLLER_H_
#define ROBOCALC_CONTROLLERS_CONTROLLER_H_

#include "Platform.h"
#include "RoboCalcAPI/Controller.h"
#include "DataTypes.h"

#include "StateMachine.h"

class Controller: public robocalc::Controller 
{
public:
	Controller(Platform& _platform) : platform(&_platform){};
	Controller() : platform(nullptr){};
	
	~Controller() = default;
	
	void Execute()
	{
		stateMachine.execute();
	}
	
	struct Channels
	{
		Controller& instance;
		Channels(Controller& _instance) : instance(_instance) {}
		
		EventBuffer* tryEmitObstacle(void* sender, std::tuple<> args)
		{
		}
		
	};
	
	Channels channels{*this};
	
	Platform* platform;
	StateMachine_StateMachine<Controller> stateMachine{*platform, *this, &stateMachine};
};

#endif
