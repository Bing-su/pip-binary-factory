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

func dummy() {
	// This is a dummy function to make the linter happy.
	// It is not used.
	_ = defaultPublicDir()
}
