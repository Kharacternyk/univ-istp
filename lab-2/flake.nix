{
  inputs.utils.url = "github:numtide/flake-utils";
  inputs.pre-commit = {
    url = "github:cachix/pre-commit-hooks.nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, utils, pre-commit }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with rec {
        fastapi-crudrouter = python310Packages.buildPythonPackage rec {
          pname = "fastapi-crudrouter";
          version = "0.8.5";
          src = python310Packages.fetchPypi {
            inherit pname version;
            format = "setuptools";
            sha256 = "unPG45gZFZpOaoeXl7eHsgV/DmvjAFy5VuIIEkNJGUI=";
          };
          propagatedBuildInputs = [
            python310Packages.fastapi
          ];
          doCheck = false;
        };
        python = python310.withPackages (pythonPackages: with pythonPackages; [
          psycopg2
          fastapi
          fastapi-crudrouter
          ormar
          uvicorn
        ]);
      }; mkShell {
        packages = [
          python
          postgresql_14
        ];
        inherit (self.checks.${system}.pre-commit) shellHook;
      };
      checks = {
        pre-commit = pre-commit.lib.${system}.run {
          src = ./.;
          hooks = {
            black.enable = true;
            nixpkgs-fmt.enable = true;
          };
        };
      };
    }
  );
}
