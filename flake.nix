{
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = pkgs.mkShell {
        packages = [
          pkgs.postgresql_14
          (pkgs.python310.withPackages (p: [ p.psycopg2 p.django ]))
        ];
      };
    }
  );
}
