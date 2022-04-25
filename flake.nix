{
  inputs.utils.url = "github:numtide/flake-utils";
  inputs.pre-commit = {
    url = "github:cachix/pre-commit-hooks.nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, utils, pre-commit }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with {
        python = pkgs.python310.withPackages (p: [ p.psycopg2 p.django ]);
      }; pkgs.mkShell {
        packages = [
          python
          pkgs.postgresql_14
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
