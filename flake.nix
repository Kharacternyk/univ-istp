{
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with {
        python = pkgs.python310.withPackages (p: [ p.psycopg2 p.django ]);
      }; pkgs.mkShell {
        packages = [
          python
          pkgs.postgresql_14
        ];
      };
    }
  );
}
