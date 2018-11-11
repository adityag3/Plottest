import _plotly_utils.basevalidators


class ShowticklabelsValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='showticklabels',
        parent_name='layout.scene.yaxis',
        **kwargs
    ):
        super(ShowticklabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
