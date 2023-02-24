{ pkgs ? import <nixpkgs> { } }:
let
  nix-alien-pkgs = import (builtins.fetchTarball
    "https://github.com/thiagokokada/nix-alien/tarball/master") { };
in pkgs.mkShell {
  NIX_LD_LIBRARY_PATH = with pkgs;
    lib.makeLibraryPath [
      at-spi2-atk.out
      cairo.out
      gdk-pixbuf.out
      glib.out
      gnome2.pango.out
      gst_all_1.gst-plugins-base.out
      gst_all_1.gstreamer.out
      gtk3.out
      harfbuzz.out
      libepoxy.out
      libgccjit.out
    ];
  NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";

  packages = with pkgs; [
    nix-alien-pkgs.nix-alien
    nix-ld
    python310Packages.pandas
  ];
}
