{
  outputs = { self, nixpkgs }: with import nixpkgs { system = "x86_64-linux"; }; {
    packages.x86_64-linux = {
      python = pkgs.python310.withPackages (p: [p.psycopg2 p.django]);
      django = pkgs.writeShellScriptBin "django" ''
        export DJANGO_SETTINGS_MODULE=istp.settings
        ${self.packages.x86_64-linux.python}/bin/python -m django "$@"
      '';
      devServer = pkgs.writeShellScriptBin "server" ''
        ${pkgs.postgresql_14}/bin/postgres -D .pgdata &
        ${self.packages.x86_64-linux.django}/bin/django runserver
      '';
      psql = pkgs.writeShellScriptBin "psql" ''
        ${pkgs.postgresql_14}/bin/psql -h "$PWD/.pgdata" -d bgclub
      '';
    };
    apps.x86_64-linux = {
      django = {
        type = "app";
        program = "${self.packages.x86_64-linux.django}/bin/django";
      };
      devServer = {
        type = "app";
        program = "${self.packages.x86_64-linux.devServer}/bin/server";
      };
      psql = {
        type = "app";
        program = "${self.packages.x86_64-linux.psql}/bin/psql";
      };
    };
  };
}
