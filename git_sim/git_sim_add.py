from manim import *
from git_sim.git_sim_base_command import GitSimBaseCommand
import git, sys, numpy

class GitSimAdd(GitSimBaseCommand):
    def __init__(self, scene):
        super().__init__(scene)
        self.maxrefs = 2

        for name in self.scene.args.name:
            if name not in [x.a_path for x in self.repo.index.diff(None)] + [z for z in self.repo.untracked_files]:
                print("git-sim error: No modified file with name: '" + name + "'")
                sys.exit()

    def execute(self):
        print("Simulating: git add " + " ".join(self.scene.args.name))

        self.show_intro()
        self.get_commits()
        self.parse_commits(self.commits[0])
        self.recenter_frame()
        self.scale_frame()
        self.vsplit_frame()
        self.setup_and_draw_zones()
        self.fadeout()
        self.show_outro()

    def populate_zones(self, firstColumnFileNames, secondColumnFileNames, thirdColumnFileNames, firstColumnArrowMap, secondColumnArrowMap):

        for x in self.repo.index.diff(None):
            if "git-sim_media" not in x.a_path:
                secondColumnFileNames.add(x.a_path)
                for name in self.scene.args.name:
                    if name == x.a_path:
                        thirdColumnFileNames.add(x.a_path)
                        secondColumnArrowMap[x.a_path] = Arrow(stroke_width=3, color=self.scene.fontColor)

        for y in self.repo.index.diff("HEAD"):
            if "git-sim_media" not in y.a_path:
                thirdColumnFileNames.add(y.a_path)

        for z in self.repo.untracked_files:
            if "git-sim_media" not in z:
                firstColumnFileNames.add(z)
                for name in self.scene.args.name:
                    if name == z:
                        thirdColumnFileNames.add(z)
                        firstColumnArrowMap[z] = Arrow(stroke_width=3, color=self.scene.fontColor)
