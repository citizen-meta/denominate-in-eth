import globals from "globals";
import pluginJs from "@eslint/js";

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  pluginJs.configs.recommended, // Recommended JavaScript rules
  {
    files: ["**/*.js"], // Apply to all JS files
    languageOptions: {
      sourceType: "commonjs", // CommonJS modules (Node.js style)
      ecmaVersion: "latest", // Support modern JavaScript syntax
      globals: {
        ...globals.node // Enable Node.js global variables like `process`
      }
    },
    rules: {
      // Add custom rules here if needed
    }
  }
];

