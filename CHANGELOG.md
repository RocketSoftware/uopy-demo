# Changelog

## UOPY 1.2.0 - Mar 24, 2022

Enhancements and fixes

- UOPY- 41 Prior to this release, uopy returned two values when only one id was sent to `read_named_fields`, and the id was not found in the file.
- UOPY- 42 This release adds a method to the `uopy.File` object that gets the fileinfo information from the server.
- UOPY- 43 An issue with the `uopy.connect` method, where turning on connection pooling was only allowed from the `uopy.ini`, has been fixed in this release. Passing `pooling_on=True` in the `uopy.connect` method will properly utilize a connection pooling license if available.
- UOPY- 66 Various performance enhancements have been made to the `uopy.File.Read` method.

### Getting fileinfo from a uopy.File object

As of uopy 1.2.0, there is a new method to get the fileinfo information for a uopy.File object. 
It gets the same information as if you were using the MultiValue BASIC FILEINFO function.

Requirements: You must be connected to a UniData 8.2.4 or later, or UniVerse 12.2.1 or later to use this feature.

In order to get the fileinfo information, you must call the uopy.File.fileInfoEx method.

<details>
<summary>Click to expand to see more information!</summary>

```python
import uopy
help(uopy.File.fileInfoEx)
```
```
Help on function fileInfoEx in module uopy._file:
fileInfoEx(self)
    Get information about the specified file’s configuration, such as the
    specified file’s parameters, its modulus and load, its operating system file name, and its VOC name.
    The information returned depends on the file type and the value of the key. After calling the method fileInfo, 
    you can access these attributes to get their values.
  
    isFileVar: 1 if file.variable is a valid file variable; 0 otherwise.
    vocName: VOC name of the file.
    pathName: Path name of the file.
    type: File type as follows: 1 Static hashed | 3 Dynamic hashed | 4 Type 1 | 5 Sequential | 7 Distributed and Multivolume
    hashAlg: Hashing algorithm: 2 for GENERAL, 3 for SEQ.NUM.
    modulus: Current modulus.
    minModulus: Minimum modulus.
    groupSize: Group size, in 1-KB units.
    largeRecordSize: Large record size.
    mergeLoad: Merge load parameter.
    splitLoad: Split load parameter.
    currentLoad: Current loading of the file (%).
    nodeName: Empty string, if the file resides on the local system, otherwise the name of the node where the file resides.
    isAKFile: 1 if secondary indexes exist on the file; 0 otherwise.
    currentLine: Current line number.
    partNum: For a distributed file, returns list of currently open part numbers.
    fileStatus: For a distributed file, returns list of status codes showing whether the last I/O operation succeeded or failed for each part. 
                A value of –1 indicates the corresponding part file is not open.
    recoveryType: 1 if the file is marked as recoverable, 0 if it is not. Returns an empty string if recoverability is not supported on the 
                  file type (such as type 1 and type 19 files).
    recoveryId: Always returns an empty string.
    isFixedModulus: Always returns 0.
    nlsmap: If NLS is enabled, the file map name, otherwise an empty string. If the map name is the default specified in the uvconfig file, 
            the returned string is the map name followed by the name of the configurable parameter in parentheses.
    encryption: Returns a dynamic array containing the following information:
            ▪ For a file encrypted with the WHOLERECORD option:
            -1@VM<key_id>@VM<algorithm>
            ▪ For a file encrypted at the field level:
            <location>@VM<key_id>@VM
            <algorithm>@VM<field_name>[@FM
            <location>...@VM<field_name>]
            ▪ Returns an empty string if the file is not encrypted.
    repStatus: Return values can be:
            0 – The file is not published, subscribed, or subwriteable.
            1 – The file is being published.
            2 – The file is being subscribed.
            3 – The file is subwriteable.
            Note: If U2 Data Replication is not running, this function
            returns 0 for any file used with this function.

    Args: void
    Returns: void
    Raise:
        UOError

    Examples:
        >>> f = uopy.File('TEST')
        >>> f.fileInfo()
        >>> print(f.vocName)
        >>> print(f.pathName)
        >>> print(f.groupSize)
```

### Checking Requirements

If you plan on using the new uopy.File.fileInfoEx method in your code, it is recommended that you check the version of uopy on the client, 
and the version of U2 on the server you are connecting to.
 
### On the Pyton client

One way to check that the correct version of uopy is installed on the client is using the pkg_resources module.

Note that there are other ways to get this information, but these have Python version requirements.

```python
import uopy
import pkg_resources 
pkg_resources.get_distribution("uopy").version
'1.2.0'
```
  
### Server-side requirements
  
In order to get the fileInfo information using the uopy.File.fileInfoEx method, you must be connected UniData 8.2.4 or UniVerse 12.2.1.

If you are on a prior release, the method will raise an uopy.UOError exception: For example:

Error [30096] : Unsupported Server Operation. This operation is not supported at this release of the server. : fileInfoEx is not supported 
on versions prior to UniData 8.2.4 or prior to UniVerse 12.2.1.

</details>

## UOPY 1.1.1 - Nov 18, 2020

Enhancement

- UOPY-38 UOPY's DynArray class should support concatenation operations like Python list

## UOPY 1.1.0 - Oct 27, 2020

- Initial release
