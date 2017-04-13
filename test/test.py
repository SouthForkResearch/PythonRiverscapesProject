import unittest


class ProjectTest(unittest.TestCase):

    def test_ProjectCreate(self):

        from Riverscapes import Project
        project = Project()

        self.assertEqual(project.name,"")
        self.assertEqual(project.projectType,"")
        self.assertEqual(project.projectVersion,"")
        project.create("ProjectName","ProjectType","1.0")
        self.assertEqual(project.name,"ProjectName")
        self.assertEqual(project.projectType,"ProjectType")
        self.assertEqual(project.projectVersion,"1.0")
        self.assertEqual(project.ProjectMetadata["RiverscapesProgramVersion"],project.riverscapes_program_version)
        self.assertEqual(project.ProjectMetadata["RiverscapesPythonProjectVersion"],project.riverscapes_python_version)

    def test_ProjectAddMetadata(self):
        from Riverscapes import Project
        project = Project()
        self.assertEqual(len(project.ProjectMetadata),0)
        project.addProjectMetadata("MetaName","MetaValue")
        self.assertEqual(project.ProjectMetadata["MetaName"],"MetaValue")

    # def test_ProjectLoadXML(self):
    #
    #     from Riverscapes import Project
    #     project = Project()
    #
    #     project.loadProjectXML()

