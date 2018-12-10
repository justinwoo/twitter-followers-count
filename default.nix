let
  pkgs = import <nixpkgs> {};
  python = pkgs.python3.withPackages(p: [
    p.requests
  ]);
in pkgs.stdenv.mkDerivation {
  name = "py-test";
  buildInputs = [
    python
  ];
}
