Class Embedded.Utils
{

ClassMethod GetNameSpace() As %Status
{

    Return $namespace
}

ClassMethod SetNameSpace(pNameSpace) As %Status
{
    zn pNameSpace
    Return $namespace
}

}
