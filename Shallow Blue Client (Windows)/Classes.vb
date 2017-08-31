Module Classes

    Class JSON_Class_Extracter

        Private C_classType As String

        Public Property classType() As String
            Get
                Return C_classType
            End Get
            Set(ByVal value As String)
                C_classType = value
            End Set
        End Property

        Private C_JSON_Text As String

        Public Property JSON_Text() As String
            Get
                Return C_JSON_Text
            End Get
            Set(ByVal value As String)
                C_JSON_Text = value
            End Set
        End Property

    End Class

    Class Temp

        Private C_tempVar As String

        Public Property tempVar() As String
            Get
                Return C_tempVar
            End Get
            Set(ByVal value As String)
                C_tempVar = value
            End Set
        End Property

    End Class

End Module
