# User Management Application

A simple user management application built with React.js that allows you to add, view, edit, and delete user information. The application features a clean and responsive interface using Material UI components.

## Features

- **User Registration**: Add new users with details such as name, email, phone, and address
- **User Listing**: View all registered users in a tabular format
- **User Management**: Edit or delete existing user information
- **Responsive Design**: Works seamlessly on both desktop and mobile devices
- **Form Validation**: Ensures valid data entry with appropriate error messages

## Live Demo

You can view and interact with the live application here: [User Management App Demo](https://harsh-tailor04.github.io/test-user/)

## Technologies Used

- **React.js**: Frontend library for building user interfaces
- **Material UI**: Component library for modern and responsive design
- **React Router**: For navigation between different views
- **LocalStorage**: For persisting user data between sessions
- **GitHub Pages**: For hosting the application

## Project Structure

```
test-user/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── components/
│   │   ├── UserForm.js
│   │   ├── UserList.js
│   │   └── ...
│   ├── App.js
│   ├── index.js
│   └── ...
├── package.json
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm or yarn

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Harsh-tailor04/test-user.git
   ```

2. Navigate to the project directory:
   ```
   cd test-user
   ```

3. Install dependencies:
   ```
   npm install
   ```
   or
   ```
   yarn install
   ```

4. Start the development server:
   ```
   npm start
   ```
   or
   ```
   yarn start
   ```

5. Open your browser and visit `http://localhost:3000`

## Deployment

This project is deployed using GitHub Pages. To deploy your own version:

1. Update the `homepage` field in `package.json`:
   ```json
   "homepage": "https://yourusername.github.io/test-user"
   ```

2. Deploy to GitHub Pages:
   ```
   npm run deploy
   ```

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- GitHub: [@Harsh-tailor04](https://github.com/Harsh-tailor04)
