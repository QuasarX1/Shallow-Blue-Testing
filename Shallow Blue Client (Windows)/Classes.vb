Module Classes

    Class Text

        Private C_text As String

        Public Property text() As String
            Get
                Return C_text
            End Get
            Set(ByVal value As String)
                C_text = value
            End Set
        End Property

    End Class

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

End Module
