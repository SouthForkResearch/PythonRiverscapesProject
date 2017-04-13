# Python Riverscapes Project
Module to read/write Rivescapes Projects (project.rs.xml) in Python

**Python Riverscapes Project Documentation** 

This module does not require any outside dependencies, and can be used to support Riverscapes projects.

Version: 1.0 2017-APR-12

**Contents**

[TOC]

------

# *Class* Project

*Riverscapes Project Class*

Represent the inputs, realizations and outputs for a confinement project and read,
write and update xml project file.

**Methods**

***Create(*** *projectName, projectType* ***)***

Used to create a new project (from scratch).

***addProjectMetadata(*** *Name, Value* ***)***

Adds Metadata to the project.

Alternative method - add to the Project.ProjectMetadata dictionary directly.

***addInputDataset(*** *name, id, relativePath, sourcePath* ***)***

Creates a dataset object and adds it as an Input Dataset to the Project (but not tied to a specific Realization).

Alternative Method - create a Dataset object then add to the Project.InputDataset dictionary directly.

***get_dataset_id(*** *filename* ***)***

Find the ID of a dataset in InputDatasets.

***loadProjectXML(*** *xmlpath* ***)***

Populate the (empty) Project object from an existing project xml.

***addRealization(*** *realization* ***)***

Adds a realization object to the Project.

***writeProjectXML(*** *xmlpath* ***)***

Saves the Project as an xml file, specified by the xml path (note this is the full path and filename)

**Properties**

***name*** string

The user provided name of the project.

***projectType*** string

The type of riverscapes project (i.e. Confinement, GNAT, etc.)

**projectPath*** string

The Base path of the project, if it was loaded from an xml file

***xmlname*** string

The name of the project xml file. This has been set to `project.rs.xml` for all projects in the Riverscapes Program.

***ProjectMetadata*** dict

A dictionary of Project Metadata.

| Keys   | Metadata Names  |
| ------ | --------------- |
| Values | Metadata Values |

***Realizations*** dict

A dictionary of Project Realizations.

| Keys   | Realization Names   |
| ------ | ------------------- |
| Values | Realization Objects |

***InputDatasets*** dict

A dictionary of all Project Input Datasets (referenced in the input xml and used in realizations).

| Keys   | Input Dataset Names |
| ------ | ------------------- |
| Values | dataset objects     |

------

# *Class* Realization

Realization objects are used to store information about a Project Realization, including inputs, parameters, outputs and analyses. The generic Realization Class can be used, or subclasses can be created for specific project types. 

**Methods**

***create(****name* ***)***

Used to create a new Realization (from scratch).

********createFromXMLElement(*** *xmlElement, dictInputDatasets* ***)*** 

Loads the information from an dataset xml node to the Realization object. 

> *This is generally used internally when a project xml file is loaded*

***getXMLNode(*** *xmlNode* ***)*** 

Adds the Realization as an xmlElement to the input xmlNode. 

> *This is generally used internally when a project xml file is getting generated.*

**Properties**

***analyses*** dict

A dictionary of Analyses in the Realization.

| Keys   | Analysis Names   |
| ------ | ---------------- |
| Values | Analysis objects |

***dateCreated*** str

The date and time stamp when the realization was created.

***guid*** str

The [guid](https://docs.python.org/2/library/uuid.html) assigned to the Realization, either when the Realization object is created, or loaded from the project xml.

***id*** str

The unique project generated ID for the Realization.

***metadata*** dict

A dictionary of Realization Metadata.

| Keys   | Metadata Names  |
| ------ | --------------- |
| Values | Metadata Values |

***name*** str

The user specified name of the Realization.

***parameters*** dict

A dictionary of parameters.

| Keys   | Parameter Names   |
| ------ | ----------------- |
| Values | Parameter Objects |

***productVersion*** str

Version of the Model or Product used to create the Realization.

***promoted*** bool

Flag indicating the Realization is the promoted one. While there should only be one promoted Realization per project, the Realization class does not check for this.

## *Subclass* GNATRealization 

**Methods**

**Properties**

## *Subclass* ConfinementRealization

**Methods**

**Properties**

------

# *Class* Analysis

An Analysis is a set of measurements, outputDatasets, and their associated parameters. An Analysis is part of a Realization in a Project, and a Realization may have any number of uniquely named Analyses.

**Methods**

***create(*** *analysis_name, analysis_type* ***)*** 

Used to create a new Analysis (from scratch).

***createFromXMLElement(*** *xmlElement* ***)*** 

Loads the information from an analysis xml node to the Analysis object. 

> *This is generally used internally when a project xml file is loaded*

***addParameter(*** *parameter_name, parameter_value* ***)*** 

Adds a parameter to the Analysis.

***getXMLNode(*** *xmlNode* ***)*** 

adds the Analysis as an xmlElement to the input xmlNode.

**Properties**

***name*** str

Name of the Analysis.

***outputDatasets*** dict

A dictionary of output Datasets in the Analysis.

| Keys   | Output Names    |
| ------ | --------------- |
| Values | Dataset Objects |

***parameters*** dict

A dictionary of parameters.

| Keys   | Parameter Names   |
| ------ | ----------------- |
| Values | Parameter Objects |

***type*** str

The Analysis Type.

------

# *Class* Dataset

A Dataset object is representation of a dataset, either as an input or output to Projects, Realizations, or Analyses.

**Methods**

***create(*** *name, relative_path, type="Vector", original_path=""* ***)***

Used to create a new Dataset object (from scratch). This will generate a new GUID to associate with the dataset.

> Note: Riverscapes Projects does not check for the existence files on disk.

***createFromXMLElement(*** *xmlElement* ***)*** 

Loads the information from an dataset xml node to the Dataset object. 

> *This is generally used internally when a project xml file is loaded*

***getXMLNode(*** *xmlNode* ***)*** 

Return the input xmlNode with the Dataset added as an xmlElement.

***absolutePath(*** *projectPath* ***)*** 

Return the absolute path of the Dataset, based on the base path of the project.

**Properties**

***guid*** str

The [guid](https://docs.python.org/2/library/uuid.html) assigned to the dataset, either when the Dataset object is created, or loaded from the project xml.

***id*** str

The Project assigned ID for the dataset.

***metadata*** dict

A dictionary of Dataset Metadata.

| Keys   | Metadata Names  |
| ------ | --------------- |
| Values | Metadata Values |

***name*** str

The name of the dataset.

***relpath*** str

The path of the dataset, relative to the project path.

***type*** str

The type of dataset, used to assign a specific xml tag to a dataset. Default type is "Vector".  



