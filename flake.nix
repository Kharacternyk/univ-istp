{
  outputs = { self, nixpkgs }: with import nixpkgs { system = "x86_64-linux"; }; {
    devShell.x86_64-linux = pkgs.mkShell {
      packages = [
        pkgs.postgresql_14
        (pkgs.python310.withPackages (p: [p.psycopg2 p.django]))
      ];
    };
  };
}
