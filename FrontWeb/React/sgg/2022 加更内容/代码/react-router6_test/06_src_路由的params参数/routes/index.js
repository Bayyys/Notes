import About from '../pages/About'
import Home from '../pages/Home'
import Message from '../pages/Message'
import News from '../pages/News'
import Detail from '../pages/Detail'
import {Navigate} from 'react-router-dom'

export default [
	{
		path:'/about',
		element:<About/>
	},
	{
		path:'/home',
		element:<Home/>,
		children:[
			{
				path:'news',
				element:<News/>
			},
			{
				path:'message',
				element:<Message/>,
				children:[
					{
						path:'detail/:id/:title/:content',
						element:<Detail/>
					}
				]
			}
		]
	},
	{
		path:'/',
		element:<Navigate to="/about"/>
	}
]