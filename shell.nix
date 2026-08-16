{ pkgs ? import <nixpkgs> {} }:

let
	# Define Python with the specific packages you need
	pythonEnv = pkgs.python3.withPackages (ps: with ps; [
		pip
		virtualenv
		numpy
		requests
		tkinter
		pytest
		pandas
		# Add other nix-packaged Python libraries here
	]);
in
pkgs.mkShell {
	# Tools available inside the shell
	packages = [
		pythonEnv
		pkgs.ruff # Linter
		pkgs.python3Packages.jedi-language-server
	];

	# Environment variables
	env = {
		PYTHONUNBUFFERED = "1";
	};

	# Hooks run when entering the shell
	shellHook = ''
		echo "Python Nix environment activated!"
		python --version
	'';
}
