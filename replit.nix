{ pkgs }: {
  deps = [
    pkgs.gdb
    pkgs.glibcLocales
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}