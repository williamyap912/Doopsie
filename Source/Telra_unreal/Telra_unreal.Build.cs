// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class Telra_unreal : ModuleRules
{
	public Telra_unreal(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "EnhancedInput" });
	}
}
