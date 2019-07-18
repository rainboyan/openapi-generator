/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package petstore
import (
	"encoding/json"
)

type List struct {
	Var123List *string `json:"123-list,omitempty"`

}

// GetVar123List returns the Var123List field if non-nil, zero value otherwise.
func (o *List) GetVar123List() string {
	if o == nil || o.Var123List == nil {
		var ret string
		return ret
	}
	return *o.Var123List
}

// GetVar123ListOk returns a tuple with the Var123List field if it's non-nil, zero value otherwise
// and a boolean to check if the value has been set.
func (o *List) GetVar123ListOk() (string, bool) {
	if o == nil || o.Var123List == nil {
		var ret string
		return ret, false
	}
	return *o.Var123List, true
}

// HasVar123List returns a boolean if a field has been set.
func (o *List) HasVar123List() bool {
	if o != nil && o.Var123List != nil {
		return true
	}

	return false
}

// SetVar123List gets a reference to the given string and assigns it to the Var123List field.
func (o *List) SetVar123List(v string) {
	o.Var123List = &v
}


func (o List) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.Var123List != nil {
		toSerialize["123-list"] = o.Var123List
	}
	return json.Marshal(toSerialize)
}


