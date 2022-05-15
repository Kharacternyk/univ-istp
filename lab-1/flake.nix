{
  inputs.utils.url = "github:numtide/flake-utils";
  inputs.pre-commit = {
    url = "github:cachix/pre-commit-hooks.nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, utils, pre-commit }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with rec {
        django-bootstrap = python310Packages.buildPythonPackage rec {
          pname = "django-bootstrap5";
          version = "21.3";
          src = python310Packages.fetchPypi {
            inherit pname version;
            format = "setuptools";
            sha256 = "NQhjQYgXgKRLLiclWJT2Ap/F73XloOyOvYL0elGE+nM=";
          };
          propagatedBuildInputs = [
            python310Packages.django
            python310Packages.beautifulsoup4
          ];
          doCheck = false;
        };
        python = python310.withPackages (pythonPackages: with pythonPackages; [
          psycopg2
          django
          django-tables2
          django-bootstrap
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
