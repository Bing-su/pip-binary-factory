package main

import (
	pb "github.com/pocketbase/pocketbase"
)

func initApp() *pb.PocketBase {
	config := pb.Config{
		DefaultDataDir: "./pb_data",
	}
	return pb.NewWithConfig(config)
}

func defaultPublicDirFix() string {
	return "./pb_public"
}
