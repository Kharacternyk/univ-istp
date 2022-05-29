{
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
    with import nixpkgs { inherit system; }; {
      devShell = with {
        server = writeShellScriptBin "server" ''
          zathura "$1" &
          ls *.tex | entr lualatex /_
        '';
      }; mkShell {
        packages = [
          entr
          server
          zathura
          liberation_ttf
          texlive.combined.scheme-full
        ];
      };
    }
  );
}
