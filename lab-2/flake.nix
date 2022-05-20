{
  inputs.utils.url = "github:numtide/flake-utils";
  inputs.pre-commit = {
    url = "github:cachix/pre-commit-hooks.nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, utils, pre-commit }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with rec {
        python = python310.withPackages (pythonPackages: with pythonPackages; [
          psycopg2
          pony
          fastapi
          uvicorn
          inflect
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
