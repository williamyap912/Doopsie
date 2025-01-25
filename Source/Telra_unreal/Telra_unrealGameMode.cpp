// Copyright Epic Games, Inc. All Rights Reserved.

#include "Telra_unrealGameMode.h"
#include "Telra_unrealCharacter.h"
#include "UObject/ConstructorHelpers.h"

ATelra_unrealGameMode::ATelra_unrealGameMode()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter"));
	if (PlayerPawnBPClass.Class != NULL)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}
}
